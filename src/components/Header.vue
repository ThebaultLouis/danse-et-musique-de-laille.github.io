<template>
  <header class="bg-white shadow-md">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <NuxtLink to="/">
        <div class="text-2xl font-bold text-gray-800">
          Danse et Musiques de Laille
        </div>
      </NuxtLink>

      <!-- Navigation Desktop -->
      <nav class="hidden md:flex space-x-6">
        <NuxtLink
          class="text-gray-700 hover:text-blue-600 transition-colors duration-300 font-medium"
          to="/cours"
        >
          Cours
        </NuxtLink>
        <NuxtLink
          class="text-gray-700 hover:text-blue-600 transition-colors duration-300 font-medium"
          to="/danses"
        >
          Danses
        </NuxtLink>
        <NuxtLink
          class="text-gray-700 hover:text-blue-600 transition-colors duration-300 font-medium"
          to="/agenda"
        >
          Agenda
        </NuxtLink>
        <NuxtLink
          class="text-gray-700 hover:text-blue-600 transition-colors duration-300 font-medium"
          to="/photos"
        >
          Photos
        </NuxtLink>
      </nav>

      <!-- Menu Mobile -->
      <div class="md:hidden">
        <button
          @click="toggleMobileMenu"
          class="text-gray-600 hover:text-gray-800 focus:outline-none"
        >
          <svg
            v-if="!isMobileMenuOpen"
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
          <svg
            v-else
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            ></path>
          </svg>
        </button>
      </div>

      <!-- Menu Mobile Dropdown -->
      <div
        v-if="isMobileMenuOpen"
        class="absolute top-16 left-0 w-full bg-white shadow-lg md:hidden"
      >
        <nav class="flex flex-col p-4 space-y-2">
          <NuxtLink to="/cours" @click="toggleMobileMenu"> Cours </NuxtLink>
          <NuxtLink to="/danses" @click="toggleMobileMenu"> Danses </NuxtLink>
          <NuxtLink to="/agenda" @click="toggleMobileMenu"> Agenda </NuxtLink>
          <NuxtLink to="/photos" @click="toggleMobileMenu"> Photos </NuxtLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>