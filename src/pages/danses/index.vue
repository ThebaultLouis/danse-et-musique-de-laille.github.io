<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-foreground">
      Nos Danses
    </h1>
    <div v-if="danses">
      <!-- Barre de recherche -->
      <div class="mb-8 flex justify-center">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Rechercher une danse..."
          class="input input-bordered w-full max-w-md bg-surface border-outline text-foreground px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-secondary"
        >
      </div>

      <!-- Tableau des danses -->
      <div class="overflow-x-auto">
        <div
          class="max-w-lg mx-auto overflow-hidden rounded-xl border border-outline shadow-md"
        >
          <table class="w-full bg-surface">
          <thead class="bg-surface-muted">
            <tr>
              <th
                class="px-4 py-3 text-left text-xs font-medium text-foreground-subtle uppercase tracking-wider"
              >
                Nom
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-outline-subtle">
            <tr
              v-for="danse in filteredDanses"
              :key="danse.id"
              class="hover:bg-background transition-colors"
            >
              <td
                class="px-4 py-4 whitespace-nowrap text-sm font-medium text-foreground"
              >
                <NuxtLink
                  :to="`danses/${danse.id}`"
                  class="hover:text-primary hover:underline"
                >
                  {{ danse.nom }}
                </NuxtLink>
              </td>
            </tr>
          </tbody>
          </table>
        </div>
      </div>

      <!-- Message si aucune danse -->
      <div
        v-if="filteredDanses.length === 0"
        class="text-center text-foreground-subtle py-12"
      >
        Aucune danse ne correspond à votre recherche.
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Danse } from "~/models";
import Fuse from "fuse.js";

useHead({
  title: "Danses - DML Country",
  meta: [
    {
      name: "description",
      content:
        "Explorez notre liste complète de danses pratiquées à DML Country.",
    },
    { property: "og:title", content: "Danses - DML Country" },
    {
      property: "og:description",
      content:
        "Explorez notre liste complète de danses country pratiquées à DML Country.",
    },
    { property: "og:type", content: "website" },
    { property: "og:url", content: "https://dml-country/danses" },
  ],
});

const options = {
  keys: ["nom"],
  threshold: 0.3,
  ignoreLocation: true,
};

const fuse = computed(() => new Fuse(danses.value || [], options));

const { data: danses } = await useFetch<Danse[]>(`/cache/danses.json`);

const searchQuery = ref("");

const filteredDanses = computed(() => {
  if (!danses.value) {
    return [];
  }
  if (!searchQuery.value.trim()) {
    return danses.value || [];
  }
  return fuse.value.search(searchQuery.value).map((result) => result.item);
});
</script>
