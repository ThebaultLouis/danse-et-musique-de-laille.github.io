<template>
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
        <PagesCoursTableItem v-for="c in cours" :key="c.id" :cours="c" />
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
const { cours } = defineProps({
  cours: Array<Cours>,
});
</script>