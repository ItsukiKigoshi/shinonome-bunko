<script setup>
  // Remember to disable the middleware protection from your page!
  definePageMeta({
    auth: { unauthenticatedOnly: true, navigateAuthenticatedTo: '/' }
  });

  const { signIn, signOut, getProviders } = useAuth();
  const providers = await getProviders();
  const { data } = useAuth();
</script>
<template>
  <v-btn v-if="data" @click="() => signOut()">
    <v-avatar size="24" v-if="data.user.image" :image="data.user.image" />
    Logout
  </v-btn>
  <v-btn
    v-else
    v-for="provider in providers"
    :key="provider.id"
    @click="signIn(provider.id)"
  >
    <v-icon>mdi-github</v-icon>
    Login with {{ provider.name }}
  </v-btn>
</template>
