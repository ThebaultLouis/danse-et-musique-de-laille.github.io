<template>
  <div>
    <ContentRenderer :value="data" />
  </div>
</template>

<script lang="ts" setup>
const { data } = await useAsyncData("pages-home", () =>
  queryCollection("pages").path("/pages/home").first()
);
</script>

<style>
</style>