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

      <div class="overflow-x-auto">
        <table
          v-if="cours"
          class="w-full bg-white shadow-md rounded-lg overflow-hidden"
        >
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
                Type
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
              v-for="cours in cours"
              :key="cours.id"
              class="hover:bg-gray-50 transition-colors"
            >
              <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ cours.date }}
              </td>
              <td class="px-4 py-4 whitespace-nowrap">
                <span class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
                  {{ cours.type }}
                </span>
              </td>
              <td class="px-4 py-4 whitespace-nowrap">
                <span
                  class="px-2 py-1 rounded-full text-xs font-medium"
                  :class="{
                    'bg-green-100 text-green-800': cours.niveau === 'Débutant',
                    'bg-yellow-100 text-yellow-800': cours.niveau === 'Novice',
                    'bg-orange-100 text-orange-800':
                      cours.niveau === 'Intermédiaire',
                  }"
                >
                  {{ cours.niveau }}
                </span>
              </td>
              <td class="px-4 py-4">
                <ul class="space-y-1">
                  <li
                    v-for="danse in cours.dansesApprises"
                    :key="danse.id"
                    class="text-gray-700"
                  >
                    <NuxtLink
                      :to="`danses/${danse.id}`"
                      class="hover:text-blue-600 hover:underline"
                    >
                      {{ danse.nom }}
                    </NuxtLink>
                  </li>
                </ul>
              </td>
              <td class="px-4 py-4">
                <ul class="space-y-1">
                  <li
                    v-for="danse in cours.dansesRevisees"
                    :key="danse.id"
                    class="text-gray-700"
                  >
                    <NuxtLink
                      :to="`danses/${danse.id}`"
                      class="hover:text-blue-600 hover:underline"
                    >
                      {{ danse.nom }}
                    </NuxtLink>
                  </li>
                </ul>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
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