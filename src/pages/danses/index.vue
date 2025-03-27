<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Nos Danses
    </h1>

    <!-- Barre de recherche -->
    <div class="mb-8 flex justify-center">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Rechercher une danse..."
        class="input input-bordered w-full max-w-md px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>

    <!-- Tableau des danses -->
    <div class="overflow-x-auto">
      <table class="w-full bg-white shadow-md rounded-lg overflow-hidden">
        <thead class="bg-gray-100">
          <tr>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Nom
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="danse in filteredDanses"
            :key="danse.id"
            class="hover:bg-gray-50 transition-colors"
          >
            <td
              class="px-4 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
            >
              <NuxtLink
                :to="`/danses/${danse.id.split('/').pop()}`"
                class="hover:text-blue-600 hover:underline"
              >
                {{ danse.nom }}
              </NuxtLink>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Message si aucune danse -->
    <div
      v-if="filteredDanses.length === 0"
      class="text-center text-gray-500 py-12"
    >
      Aucune danse ne correspond à votre recherche.
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Danse } from "~/content/schemas";

const { data: danses } = await useAsyncData("danses", () =>
  queryCollection("danses").all()
);

const searchQuery = ref("");

const filteredDanses = computed(() => {
  return danses.value?.filter((danse: Danse) =>
    danse.nom.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});
</script>