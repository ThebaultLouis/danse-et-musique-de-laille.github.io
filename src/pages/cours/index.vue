<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Historique des Cours
    </h1>
    <div v-if="cours">
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
          v-model="selectedDate"
          class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
        >
          <option value="">Tous les jours</option>
          <option
            v-for="date in new Set(cours.map((cours) => cours.date))"
            :key="date"
            :value="date"
          >
            {{ date }}
          </option>
        </select>
      </div>

      <PagesCoursTable :cours="filteredCours" />
    </div>
  </div>
</template>

<script setup lang="ts">
const { data: cours } = await useFetch<Cours[]>(`/cache/cours.json`);

const selectedNiveau = ref("");
const selectedType = ref("");
const selectedDate = ref("");

const filteredCours = computed(() => {
  if (!cours.value) {
    return [];
  }
  return cours.value!.filter(
    (cours) =>
      !selectedNiveau.value ||
      (cours.niveau === selectedNiveau.value &&
        (!selectedType.value || cours.type === selectedType.value) &&
        (!selectedDate.value || cours.date === selectedDate.value))
  );
});
</script>