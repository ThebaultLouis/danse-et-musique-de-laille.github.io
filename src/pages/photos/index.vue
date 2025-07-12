<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-gray-800">
      Albums photos
    </h1>
    <div class="overflow-x-auto flex justify-center">
      <table
        v-if="sortedAlbums"
        class="w-full max-w-xl bg-white shadow-md rounded-lg overflow-hidden"
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
              Nom
            </th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200">
          <tr
            v-for="album in albums"
            :key="album.id"
            class="hover:bg-gray-50 transition-colors cursor-pointer"
            @click="$router.push(`/photos/${album.id}`)"
          >
            <td class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
              {{ album.date }}
            </td>
            <td class="px-4 py-4 whitespace-nowrap">
              <span class="px-4 py-4 whitespace-nowrap text-sm text-gray-600">
                {{ album.name }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data: albums } = await useFetch<Album[]>(`/cache/albums.json`);

const sortedAlbums = computed(() => {
  if (!albums.value) {
    return [];
  }
  return albums.value.sort((a: Album, b: Album) =>
    b.date.localeCompare(a.date)
  );
});
</script>