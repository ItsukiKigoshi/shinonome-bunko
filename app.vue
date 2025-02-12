<script setup lang="ts">
  useSeoMeta({
    title: '東雲文庫/Shinonome Bunko',
    ogTitle: '東雲文庫/Shinonome Bunko',
    description:
      'OCR&Git-powered Kosakuin (Contributor) for Aozora Bunko. / 青空文庫の耕作に貢献するべく，OCR技術を用いたテキスト電子化を試みる極めて私的なプロジェクト．',
    ogDescription:
      'OCR&Git-powered Kosakuin (Contributor) for Aozora Bunko. / 青空文庫の耕作に貢献するべく，OCR技術を用いたテキスト電子化を試みる極めて私的なプロジェクト．'
    // ogImage: 'https://example.com/image.png',
    // twitterCard: 'summary_large_image',
  });
</script>
<template>
  <NuxtLayout>
    <v-responsive class="border rounded">
      <v-app>
        <v-app-bar>
          <v-app-bar-title>
            <NuxtLink to="/">東雲文庫/Shinonome Bunko (Preview)</NuxtLink>
            <v-btn
              href="https://github.com/itsukikigoshi/shinonome-bunko"
              icon="mdi-github"
              target="_blank"
            ></v-btn>
          </v-app-bar-title>
          <v-spacer />
          <SiginInBtn />
        </v-app-bar>
        <v-main>
          <NuxtPage />
        </v-main>
      </v-app>
    </v-responsive>
  </NuxtLayout>
</template>
