<script>
  import axios from 'axios';
  import 'tify';
  import 'tify/dist/tify.css';
  import { Octokit } from '@octokit/rest';
  import { Buffer } from 'buffer';
  import { config } from 'dotenv';

  export default {
    data() {
      return {
        cachedResponse: {},
        commiter: {
          name: '',
          email: ''
        },
        commitDestination: '',
        commitMessage: '',
        text: '',
        tify: null
      };
    },
    methods: {
      async fetchData() {
        try {
          const owner = 'itsukikigoshi';
          const repo = 'shinonome-storage';
          this.tify.ready.then(async () => {
            const path =
              this.$route.params.org +
              '/' +
              this.$route.params.id +
              '/' +
              this.tify.options.pages[0] +
              '.txt';
            const octokit = new Octokit({
              auth: config.githubOauthToken
            });
            let file;
            try {
              file = await octokit.rest.repos.getContent({
                owner: owner,
                repo: repo,
                path: path
              });
            } catch (e) {
              if (e.status !== 404) {
                throw e;
              }
              file = null;
            }
            // When file exists on GitHub, use it as the initial text
            if (file) {
              console.log('file exists');
              const github_response = await axios.get(file.data.download_url);
              console.log(github_response.data);
              this.text = github_response.data;
            } else if (this.cachedResponse.length > 0) {
              console.log('cached response');
              // Use cached response if available
              this.tify.ready.then(() => {
                this.text = this.cachedResponse.find(
                  item => item.page === this.tify.options.pages[0]
                ).contents;
              });
            } else {
              console.log('fetching data');
              // Fetch data from API
              const ndl_response = await axios.get(
                'https://lab.ndl.go.jp/dl/api/book/fulltext-json/1823865'
              );
              const object = ndl_response.data.list;
              // Cache the response
              this.cachedResponse = object;
              // Set the text
              this.tify.ready.then(() => {
                this.text = object.find(
                  item => item.page === this.tify.options.pages[0]
                ).contents;
              });
            }
            this.tify.ready.then(() => {
              this.commitDestination =
                'https://github.com/itsukikigoshi/shinonome-storage/blob/main/' +
                this.$route.params.org +
                '/' +
                this.$route.params.id +
                '/' +
                this.tify.options.pages[0] +
                '.txt';
              this.commitMessage =
                'Update ' +
                this.$route.params.org +
                '/' +
                this.$route.params.id +
                '/' +
                this.tify.options.pages[0] +
                '.txt';
            });
          });
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      changePage(num) {
        this.tify.ready.then(() => {
          if (this.tify.options.pages[0] + num > 0) {
            this.tify.setPage(this.tify.options.pages[0] + num);
            this.fetchData();
          }
        });
      },
      createGitHubCommit() {
        const owner = 'itsukikigoshi';
        const repo = 'shinonome-storage';
        this.tify.ready.then(async () => {
          const path =
            this.$route.params.org +
            '/' +
            this.$route.params.id +
            '/' +
            this.tify.options.pages[0] +
            '.txt';
          const octokit = new Octokit({
            auth: config.githubOauthToken
          });
          let file;
          try {
            file = await octokit.rest.repos.getContent({
              owner: owner,
              repo: repo,
              path: path
            });
          } catch (e) {
            if (e.status !== 404) {
              throw e;
            }
            file = null;
          }

          const response = await octokit.repos.createOrUpdateFileContents({
            owner: owner,
            repo: repo,
            path: path,
            content: Buffer.from(this.text).toString('base64'),
            message: this.commitMessage,
            committer: {
              name: this.commiter.name,
              email: this.commiter.email
            },
            author: {
              name: this.commiter.name,
              email: this.commiter.email
            },
            sha: file ? file.data.sha : null
          });
          console.log(response);
        });
      }
    },
    mounted() {
      // TODO - Make a function to add manifestUrl based on whether the book is in the NDL or not
      this.tify = new Tify({
        manifestUrl:
          'https://www.dl.ndl.go.jp/api/iiif/' +
          this.$route.params.id +
          '/manifest.json',
        viewer: {
          immediateRender: false
        }
      });
      this.tify.mount('#tify');
      this.fetchData();
    }
  };
</script>
<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <div id="tify" style="height: 80vh"></div>
        <v-btn @click="changePage(1)">Next</v-btn>
        <v-btn @click="changePage(-1)">Previous</v-btn>
      </v-col>
      <v-col cols="6">
        <form>
          <v-text-field
            label="DOI"
            :model-value="$route.params.org + '/' + $route.params.id"
            readonly
          ></v-text-field>
          <v-text-field
            label="Title / Author"
            model-value="蝸牛考 (言語誌叢刊) / 柳田國男"
            readonly
          ></v-text-field>
          <v-text-field
            label="Page"
            :model-value="
              this.tify &&
              this.tify.options &&
              this.tify.options.pages &&
              this.tify.options.pages[0]
            "
            readonly
          ></v-text-field>
          <v-textarea label="Text" v-model="text"></v-textarea>
          <v-text-field
            label="Commiter Name"
            v-model="commiter.name"
          ></v-text-field>
          <v-text-field
            label="Commiter Email"
            v-model="commiter.email"
          ></v-text-field>
          <v-textarea
            label="Commit Message"
            v-model="commitMessage"
          ></v-textarea>
          <v-btn @click.prevent="createGitHubCommit" color="primary">
            Commit
          </v-btn>
        </form>
        <p>
          Commit Destination:
          <NuxtLink :to="this.commitDestination" target="_blank">
            {{ this.commitDestination }}
          </NuxtLink>
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
