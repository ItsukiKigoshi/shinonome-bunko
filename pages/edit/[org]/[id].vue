<script setup lang="ts">
  import axios from 'axios';
  import 'tify';
  import 'tify/dist/tify.css';
  import { Octokit } from '@octokit/rest';
  import { Buffer } from 'buffer';
  const route = useRoute();
  let tify;
  onMounted(() => {
    tify = new Tify({
      manifestUrl: `https://www.dl.ndl.go.jp/api/iiif/${route.params.id}/manifest.json`,
      viewer: {
        immediateRender: false
      }
    });
    tify.mount('#tify');
    fetchData();
  });

  // Is it a good use case of "let" to declare these variables?
  const text = defineModel('text', {
    type: String,
    default: ''
  });
  const commiterName = defineModel('commiterName', {
    type: String,
    default: ''
  });
  const commiterEmail = defineModel('commiterEmail', {
    type: String,
    default: ''
  });
  const commitMessage = defineModel('commitMessage', {
    type: String,
    default: ''
  });
  const cachedResponse = defineModel('cachedResponse', {
    type: Object,
    default: {}
  });
  const commitDestination = defineModel('commitDestination', {
    type: String,
    default: ''
  });

  const fetchData = () => {
    try {
      const owner = 'itsukikigoshi';
      const repo = 'shinonome-storage';
      tify.ready.then(async () => {
        const path = `${route.params.org}/${route.params.id}/${tify.options.pages[0]}.txt`;
        const octokit = new Octokit({
          auth: '' // TODO - Add GitHub OAuth token
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
          text.value = github_response.data;
        } else if (cachedResponse.value.length > 0) {
          console.log('cached response');
          // Use cached response if available
          tify.ready.then(() => {
            text.value = cachedResponse.value.find(
              item => item.page === tify.options.pages[0]
            ).contents;
          });
        } else {
          console.log('fetching data');
          // Fetch data from API
          const ndl_response = await axios.get(
            `https://lab.ndl.go.jp/dl/api/book/fulltext-json/${route.params.id}`
          );
          const object = ndl_response.data.list;
          // Cache the response
          cachedResponse.value = object;
          // Set the text
          tify.ready.then(() => {
            text.value = object.find(
              item => item.page === tify.options.pages[0]
            ).contents;
          });
        }
        tify.ready.then(() => {
          commitDestination.value = `https://github.com/itsukikigoshi/shinonome-storage/blob/main/${route.params.org}/${route.params.id}/${tify.options.pages[0]}.txt`;
          commitMessage.value = `Update ${route.params.org}/${route.params.id}/${tify.options.pages[0]}.txt`;
        });
      });
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const changePage = num => {
    tify.ready.then(() => {
      if (tify.options.pages[0] + num > 0) {
        tify.setPage(tify.options.pages[0] + num);
        fetchData();
      }
    });
  };

  const createGitHubCommit = () => {
    const owner = 'itsukikigoshi';
    const repo = 'shinonome-storage';
    tify.ready.then(async () => {
      const path = `${route.params.org}/${route.params.id}/${tify.options.pages[0]}.txt`;
      const octokit = new Octokit({
        auth: '' // TODO - Add GitHub OAuth token
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
        content: Buffer.from(text).toString('base64'),
        message: commitMessage,
        committer: {
          name: commiterName,
          email: commiterEmail
        },
        author: {
          name: commiterName,
          email: commiterEmail
        },
        sha: file ? file.data.sha : null
      });
      console.log(response);
    });
  };
</script>
<template>
  <p>{{ route.params.id }}</p>
  <p>Your Name is {{ commiterName }}</p>
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
              tify &&
              tify.options &&
              tify.options.pages &&
              tify.options.pages[0]
            "
            readonly
          ></v-text-field>
          <v-textarea label="Text" v-model="text"></v-textarea>
          <v-text-field
            label="Commiter Name"
            v-model="commiterName"
          ></v-text-field>
          <v-text-field
            label="Commiter Email"
            v-model="commiterEmail"
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
          <NuxtLink :to="commitDestination" target="_blank">
            {{ commitDestination }}
          </NuxtLink>
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>
