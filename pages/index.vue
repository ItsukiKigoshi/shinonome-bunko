<script setup>
const items = [
  'Item 1',
  'Item 2',
  'Item 3',
  'Item 4',
]
</script>
<template>
  <v-responsive class="border rounded">
    <v-app>
      <v-app-bar>
        <v-app-bar-title>東雲文庫/Shinonome Bunko</v-app-bar-title>
      </v-app-bar>
      <v-main>
        <v-container>
          <v-row>
            <h1>東雲文庫</h1>
          </v-row>
          <v-row>
            <v-col cols="6">
              Here are the Photos of Books
              <!--              <MiradorViewer/>-->
            </v-col>
            <v-col cols="6">
              <form>
                <v-text-field label="DOI" model-value="10.11501/1823865" readonly></v-text-field>
                <v-text-field label="Title" model-value="蝸牛考 (言語誌叢刊)" readonly></v-text-field>
                <v-select
                    :items="items"
                    label="Branch"
                ></v-select>
                <v-textarea auto-grow label="Text"></v-textarea>
                <v-text-field label="Commit Message"></v-text-field>
                <v-btn>Commit</v-btn>
              </form>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </v-responsive>
</template>