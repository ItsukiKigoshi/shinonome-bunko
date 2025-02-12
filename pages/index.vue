<script setup>
  const { data } = useAuth();
</script>
<template>
  <v-main>
    <div v-if="data">Hello {{ data.user.name }}!</div>
    <div v-else>You are not logged in.</div>
    <v-card class="mx-auto" max-width="344">
      <v-img
        height="200px"
        src="https://dl.ndl.go.jp/api/iiif/1823865/R0000001/full/full/0/default.jpg"
        cover
      ></v-img>
      <v-card-title>蝸牛考 / 柳田国男</v-card-title>
      <v-card-subtitle>国立国会図書館</v-card-subtitle>
      <v-card-actions>
        <NuxtLink to="/edit/10.11501/1823865">
          <v-btn text="Edit"></v-btn>
        </NuxtLink>
      </v-card-actions>
    </v-card>
  </v-main>
</template>
