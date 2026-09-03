<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-4xl font-bold text-center mb-12 text-foreground">
      Albums photos
    </h1>
    <div class="overflow-x-auto">
      <div
        v-if="sortedAlbums"
        class="max-w-xl mx-auto overflow-hidden rounded-xl border border-outline shadow-md"
      >
        <table class="w-full bg-surface">
          <thead class="bg-surface-muted">
          <tr>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-foreground-subtle uppercase tracking-wider"
            >
              Date
            </th>
            <th
              class="px-4 py-3 text-left text-xs font-medium text-foreground-subtle uppercase tracking-wider"
            >
              Nom
            </th>
          </tr>
          </thead>
          <tbody class="divide-y divide-outline-subtle">
          <tr
            v-for="album in sortedAlbums"
            :key="album.id"
            class="hover:bg-background transition-colors cursor-pointer"
            @click="$router.push(`/photos/${album.id}`)"
          >
            <td class="px-4 py-4 whitespace-nowrap text-sm text-foreground-subtle">
              {{ album.date }}
            </td>
            <td class="px-4 py-4 whitespace-nowrap">
              <span class="px-4 py-4 whitespace-nowrap text-sm text-foreground-muted">
                {{ album.name }}
              </span>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data: albums } = await useFetch<Album[]>(`/cache/albums.json`);

const sortedAlbums = computed(() => {
  if (!albums.value) {
    return [];
  }
  return [...albums.value].sort((a: Album, b: Album) =>
    b.date.localeCompare(a.date)
  );
});
</script>
