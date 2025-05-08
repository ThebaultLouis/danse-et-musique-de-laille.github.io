<template>
  <tr v-if="cours" class="hover:bg-gray-50 transition-colors">
    <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
      {{ cours.dateRealisation }}
    </td>
    <td class="px-4 py-4 whitespace-nowrap">
      <span class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
        {{ cours.collectionItem.type }}
      </span>
    </td>
    <td class="px-4 py-4 whitespace-nowrap">
      <span
        class="px-2 py-1 rounded-full text-xs font-medium"
        :class="{
          'bg-green-100 text-green-800':
            cours.collectionItem.niveau === 'Débutant',
          'bg-yellow-100 text-yellow-800':
            cours.collectionItem.niveau === 'Novice',
          'bg-orange-100 text-orange-800':
            cours.collectionItem.niveau === 'Intermédiaire',
        }"
      >
        {{ cours.collectionItem.niveau }}
      </span>
    </td>
    <td class="px-4 py-4">
      <ul class="space-y-1">
        <li
          v-for="danse in cours.collectionItem.danses_apprises"
          :key="danse"
          class="text-gray-700"
        >
          <NuxtLink :to="danse" class="hover:text-blue-600 hover:underline">
            {{ Cours.dancePathToDanceName(danse) }}
          </NuxtLink>
        </li>
      </ul>
    </td>
    <td class="px-4 py-4">
      <ul class="space-y-1">
        <li
          v-for="danse in cours.collectionItem.danses_revisees"
          :key="danse"
          class="text-gray-700"
        >
          <NuxtLink :to="danse" class="hover:text-blue-600 hover:underline">
            {{ Cours.dancePathToDanceName(danse) }}
          </NuxtLink>
        </li>
      </ul>
    </td>
  </tr>
</template>

<script setup lang="ts">
import { Cours } from "~/models";

const { cours } = defineProps({
  cours: Cours,
});
</script>