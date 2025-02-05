<script>
import axios from 'axios';
import "tify";
import "tify/dist/tify.css";

export default {
data() {
    return {
      text: '',
      items: ['master', 'develop'],
      page: 1,
      tify: null
    };
  },
  methods: {
    async fetchData() {
      try {
        // TODO - ページ更新ごとにfetchするのは非効率なので、キャッシュする
        // APIのURLにGETリクエストを送信
        const response = await axios.get('https://lab.ndl.go.jp/dl/api/book/fulltext-json/1823865');
        const object = response.data.list.find(item => item.page === this.page);
        console.log(JSON.stringify(object.contents));
        // APIから返ってきたデータをtextにセット
        // this.text = JSON.stringify(response.data);
        this.text = object.contents;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    changePage(page) {
      this.fetchData();
      this.tify.setPage(page);
    },
  },
  mounted() {
    this.fetchData();
    this.tify = new Tify({
      manifestUrl: "https://www.dl.ndl.go.jp/api/iiif/1823865/manifest.json",
      viewer: {
        immediateRender: false,
      },
    });
    this.tify.mount('#tify');
  }
}
</script>
<template>
  
  <v-container>
    <v-row>
      <v-col cols="8">
        <p>Current Page: {{ this.page }}</p>
          <div id="tify" style="height: 80vh"></div>                
          <v-btn @click="page += 1; changePage(this.page);">Next</v-btn>
        <v-btn @click="page -= 1; changePage(this.page);">Previous</v-btn>    
      </v-col>
      <v-col cols="4">
        <form>
          <v-text-field label="DOI" model-value="10.11501/1823865" readonly></v-text-field>
          <v-text-field label="Title" model-value="蝸牛考 (言語誌叢刊)" readonly></v-text-field>
          <v-select
              :items="items"
              label="Branch"
          ></v-select>
          <v-textarea label="Text" :model-value="text"
          ></v-textarea>
          <v-text-field label="Commit Message"></v-text-field>
          <v-btn>Commit</v-btn>
        </form>
      </v-col>
    </v-row>
  </v-container>
</template>