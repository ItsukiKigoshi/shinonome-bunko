<script setup lang="ts">
  const headers = useRequestHeaders(['cookie']) as HeadersInit;
  const { data: token } = await useFetch('/api/token', { headers });
</script>

<template>
  <div>{{ token || 'no token present, are you logged in?' }}</div>
</template>
