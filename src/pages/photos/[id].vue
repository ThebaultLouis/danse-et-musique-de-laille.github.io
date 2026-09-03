<template>
  <div class="p-6 max-w-7xl mx-auto">
    <NuxtLink
      to="/photos"
      class="font-medium text-primary hover:text-primary-dark hover:underline mb-4 inline-block"
    >
      Retour aux photos
    </NuxtLink>

    <h1 class="text-2xl font-bold mb-2">{{ album.name }}</h1>
    <p class="text-foreground-subtle mb-6">{{ album.date }}</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      <div
        v-for="(photo, index) in filteredPhotos"
        :key="index"
        class="relative w-full aspect-square overflow-hidden rounded"
      >
        <div
          v-if="photo.endsWith('.pdf')"
          class="flex flex-col items-center justify-center bg-surface border border-outline rounded-xl p-4 text-center w-full h-full"
        >
          <a
            :href="photo"
            target="_blank"
            class="mt-2 text-primary text-sm underline hover:text-primary-dark"
          >
            Open PDF
          </a>
        </div>

        <img
          v-else
          :src="photo"
          loading="lazy"
          class="rounded shadow object-cover w-full h-full cursor-pointer hover:scale-105 transition"
          @click="openFullscreen(index)"
        >
      </div>
    </div>

    <!-- Lightbox -->
    <div
      v-if="fullscreenPhoto"
      class="fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center"
      @click="closeFullscreen"
    >
      <img
        :src="fullscreenPhoto"
        class="max-w-full max-h-full object-contain rounded"
      >
      <button
        class="absolute top-4 left-4 bg-background text-foreground hover:bg-surface-muted px-3 py-1 rounded-lg shadow transition-colors"
        @click.stop="closeFullscreen"
      >
        Fermer
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute } from "vue-router";
import { computed } from "vue";

const { data: albums } = await useFetch<Album[]>(`/cache/albums.json`);
const route = useRoute();
const albumId = route.params.id;
const album = computed(() => albums.value?.find((a) => a.id === albumId));

const filteredPhotos = computed(() => album.value?.photos);

const fullscreenPhoto = ref(null);
const currentIndex = ref(-1);

const openFullscreen = (index: number) => {
  currentIndex.value = index;
  fullscreenPhoto.value = filteredPhotos.value[index];
};

const closeFullscreen = () => {
  fullscreenPhoto.value = null;
  currentIndex.value = -1;
};

const onKeyDown = (event) => {
  if (!fullscreenPhoto.value) return;

  if (event.key === "ArrowRight") {
    // Move to next image
    currentIndex.value = (currentIndex.value + 1) % filteredPhotos.value.length;
    fullscreenPhoto.value = filteredPhotos.value[currentIndex.value];
  } else if (event.key === "ArrowLeft") {
    // Move to previous image
    currentIndex.value =
      (currentIndex.value - 1 + filteredPhotos.value.length) %
      filteredPhotos.value.length;
    fullscreenPhoto.value = filteredPhotos.value[currentIndex.value];
  } else if (event.key === "Escape") {
    closeFullscreen();
  }
};

onMounted(() => {
  window.addEventListener("keydown", onKeyDown);
});

onBeforeUnmount(() => {
  window.removeEventListener("keydown", onKeyDown);
});
</script>
