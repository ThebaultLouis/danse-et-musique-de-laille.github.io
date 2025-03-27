<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Historique des Cours
    </h1>

    <!-- Filtres et recherche -->
    <div class="mb-8 flex justify-center space-x-4">
      <select
        v-model="selectedNiveau"
        class="select select-bordered w-full max-w-xs px-4 py-2 border rounded-lg"
      >
        <option value="">Tous niveaux</option>
        <option value="BEGINNER">Débutant</option>
        <option value="INTERMEDIATE">Intermédiaire</option>
        <option value="ADVANCED">Avancé</option>
      </select>
    </div>

    <!-- Liste des cours -->
    <div class="space-y-6">
      <div
        v-for="cours in filteredCours"
        :key="cours._path"
        class="bg-white shadow-lg rounded-lg p-6 hover:shadow-xl transition-shadow"
      >
        <div class="flex justify-between items-center mb-4">
          <span class="badge badge-primary">
            Niveau: {{ getNiveauLibelle(cours.niveau) }}
          </span>
          <span class="text-gray-500">
            {{ formatDate(cours.date_realisation) }}
          </span>
        </div>

        <div class="mb-4">
          <h2 class="text-xl font-semibold text-gray-800 mb-2">
            Danses Révisées
          </h2>
          <ul class="list-disc list-inside text-gray-700">
            <li v-for="danse in cours.danses_revisees" :key="danse">
              {{ danse }}
            </li>
          </ul>
        </div>

        <div>
          <h2 class="text-xl font-semibold text-gray-800 mb-2">
            Danses Apprises
          </h2>
          <ul class="list-disc list-inside text-gray-700">
            <li v-for="danse in cours.danse_apprise" :key="danse">
              {{ danse }}
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Message si aucun cours -->
    <div
      v-if="filteredCours.length === 0"
      class="text-center text-gray-500 py-12"
    >
      Aucun cours ne correspond à votre sélection.
    </div>
  </div>
</template>

<script setup lang="ts">
const { data: cours } = await useAsyncData("cours", () =>
  queryContent("cours").find()
);

const selectedNiveau = ref("");

const filteredCours = computed(() => {
  return cours.filter(
    (c) => !selectedNiveau.value || c.niveau === selectedNiveau.value
  );
});

const getNiveauLibelle = (niveau) => {
  const niveaux = {
    BEGINNER: "Débutant",
    INTERMEDIATE: "Intermédiaire",
    ADVANCED: "Avancé",
  };
  return niveaux[niveau] || niveau;
};

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString("fr-FR", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
  });
};
</script>