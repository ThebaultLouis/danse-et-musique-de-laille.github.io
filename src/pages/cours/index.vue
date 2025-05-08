<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Historique des Cours
    </h1>

    <PagesCoursTable :cours-collection="coursCollection" />
  </div>
</template>

<script setup lang="ts">
import { CoursCollection } from "~/models";

const { data } = await useAsyncData("cours", () =>
  queryCollection("cours").all()
);

const coursCollection: CoursCollection =
  CoursCollection.fromCoursCollectionItems(data.value);
</script>