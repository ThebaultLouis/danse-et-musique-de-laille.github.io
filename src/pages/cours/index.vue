<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Historique des Cours
    </h1>

    <div class="mb-8 flex justify-center space-x-4">
      <select
        v-model="selectedNiveau"
        class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
      >
        <option value="">Tous les niveaux</option>
        <option value="Débutant">Débutant</option>
        <option value="Intermédiaire">Intermédiaire</option>
        <option value="Avancé">Avancé</option>
      </select>

      <select
        v-model="selectedType"
        class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
      >
        <option value="">Tous les types</option>
        <option value="Country">Country</option>
        <option value="Catalan">Catalan</option>
      </select>

      <select
        type="date"
        v-model="selectedDate"
        class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
      >
        <option value="">Tous les jours</option>
        <option
          v-for="date in new Set(
            coursCollection.items.map((cours) => cours.dateRealisation)
          )"
          :key="date"
          :value="date"
        >
          {{ date }}
        </option>
      </select>
    </div>

    <PagesCoursTable :cours="filteredCours" />
  </div>
</template>

<script setup lang="ts">
import { CoursCollection } from "~/models";

const { data } = await useAsyncData("cours", () =>
  queryCollection("cours").order("date_realisation", "DESC").all()
);

const coursCollection: CoursCollection =
  CoursCollection.fromCoursCollectionItems(data.value);

const selectedNiveau = ref("");
const selectedType = ref("");
const selectedDate = ref("");

const filteredCours = computed(() => {
  return coursCollection.items.filter(
    (cours) =>
      (!selectedNiveau.value ||
        cours.collectionItem.niveau === selectedNiveau.value) &&
      (!selectedType.value ||
        cours.collectionItem.type === selectedType.value) &&
      (!selectedDate.value || cours.dateRealisation === selectedDate.value)
  );
});
</script>