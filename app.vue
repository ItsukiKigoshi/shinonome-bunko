<template>
  <NuxtLayout>
    <v-responsive class="border rounded">
      <v-app>
        <v-app-bar>
          <v-app-bar-title>
            <NuxtLink to="/">東雲文庫/Shinonome Bunko</NuxtLink>
          </v-app-bar-title>
          <v-spacer />
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
