<template>
  <NuxtLayout>
    <v-responsive class="border rounded">
      <v-app>
        <v-app-bar>
          <v-app-bar-title>東雲文庫/Shinonome Bunko</v-app-bar-title>
          <v-btn
            href="https://github.com/itsukikigoshi/shinonome-bunko"
            icon="mdi-github"
            target="_blank"
          ></v-btn>
        </v-app-bar>
        <v-main>
          <NuxtPage />
        </v-main>
      </v-app>
    </v-responsive>
  </NuxtLayout>
</template>
