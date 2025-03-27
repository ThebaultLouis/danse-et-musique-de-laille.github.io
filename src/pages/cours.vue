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

    <!-- Tableau des cours -->
    <div class="overflow-x-auto">
      <table class="w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead class="bg-gray-100">
          <tr>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Date
            </th>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Niveau
            </th>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Danses Apprises
            </th>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Danses Révisées
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="cours in filteredCours"
            :key="cours._path"
            class="hover:bg-gray-50 transition-colors"
          >
            <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
              {{ formatDate(cours.date_realisation) }}
            </td>
            <td class="px-4 py-4 whitespace-nowrap">
              <span
                class="px-2 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800"
              >
                {{ getNiveauLibelle(cours.niveau) }}
              </span>
            </td>
            <td class="px-4 py-4">
              <ul class="space-y-1">
                <li
                  v-for="danse in cours.danses_apprises"
                  :key="danse"
                  class="text-sm text-gray-700"
                >
                  <NuxtLink
                    :to="getDanseLink(danse)"
                    class="hover:text-blue-600 hover:underline"
                  >
                    {{ danse }}
                  </NuxtLink>
                </li>
              </ul>
            </td>
            <td class="px-4 py-4">
              <ul class="space-y-1">
                <li
                  v-for="danse in cours.danses_revisees"
                  :key="danse"
                  class="text-sm text-gray-700"
                >
                  <NuxtLink
                    :to="getDanseLink(danse)"
                    class="hover:text-blue-600 hover:underline"
                  >
                    {{ danse }}
                  </NuxtLink>
                </li>
              </ul>
            </td>
          </tr>
        </tbody>
      </table>
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
  queryCollection("cours").all()
);

const selectedNiveau = ref("");

const filteredCours = computed(() => {
  return cours.value?.filter(
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

const getDanseLink = (dansePath) => {
  // Extrait l'identifiant de la danse du chemin
  const match = dansePath.match(/danses\/(.+)/);
  return match ? `/danses/${match[1]}` : "#";
};
</script>