<script>
  import axios from 'axios';
  import 'tify';
  import 'tify/dist/tify.css';

  export default {
    data() {
      return {
        cachedResponse: {},
        items: ['master', 'develop'],
        text: '',
        tify: null
      };
    },
    methods: {
      async fetchData() {
        try {
          if (this.cachedResponse.length > 0) {
            console.log('Using cached response');
            // Use cached response if available
            this.tify.ready.then(() => {
              this.text = this.cachedResponse.find(
                item => item.page === this.tify.options.pages[0]
              ).contents;
            });
          } else {
            console.log('Fetching data from API');
            // Fetch data from API
            const response = await axios.get(
              'https://lab.ndl.go.jp/dl/api/book/fulltext-json/1823865'
            );
            const object = response.data.list;
            // Cache the response
            this.cachedResponse = object;
            // Set the text
            this.tify.ready.then(() => {
              this.text = object.find(
                item => item.page === this.tify.options.pages[0]
              ).contents;
            });
          }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      changePage(num) {
        this.tify.ready.then(() => {
          if (this.tify.options.pages[0] + num > 0) {
            console.log(this.tify.options.pages[0]);
            this.tify.setPage(this.tify.options.pages[0] + num);
            this.fetchData();
          }
        });
      }
    },
    mounted() {
      this.fetchData();
      this.tify = new Tify({
        manifestUrl: 'https://www.dl.ndl.go.jp/api/iiif/1823865/manifest.json',
        viewer: {
          immediateRender: false
        }
      });
      this.tify.mount('#tify');
    }
  };
</script>
<template>
  <v-container>
    <v-row>
      <v-col cols="6">
        <p v-if="this.tify && this.tify.options.pages">
          Current Page: {{ this.tify.options.pages[0] }}
        </p>
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
            label="Title"
            model-value="蝸牛考 (言語誌叢刊)"
            readonly
          ></v-text-field>
          <v-select :items="items" label="Branch"></v-select>
          <v-textarea label="Text" :model-value="text"></v-textarea>
          <v-text-field label="Commit Message"></v-text-field>
          <v-btn>Commit</v-btn>
        </form>
      </v-col>
    </v-row>
  </v-container>
</template>
