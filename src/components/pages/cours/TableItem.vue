<template>
  <tr v-if="cours" class="hover:bg-gray-50 transition-colors">
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
          'bg-orange-100 text-orange-800': cours.niveau === 'Intermédiaire',
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
</template>

<script setup lang="ts">
import { defineProps, type PropType } from "vue";
import type { Cours } from "~/models";

const { cours } = defineProps({
  cours: Object as PropType<Cours>,
});
</script>