<template>
  <header
    class="z-50 w-full transition-colors duration-300"
    :class="
      isHomePage
        ? 'absolute top-0 left-0 bg-gradient-to-b from-black/60 to-transparent'
        : 'relative bg-background shadow-md'
    "
  >
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <NuxtLink to="/">
        <div
          class="text-2xl font-bold transition-colors"
          :class="isHomePage ? 'text-white drop-shadow-md' : 'text-foreground'"
        >
          Danse et Musiques de Laille
        </div>
      </NuxtLink>

      <!-- Navigation Desktop -->
      <nav class="hidden md:flex space-x-6">
        <NuxtLink
          :class="navLinkClasses"
          to="/cours"
        >
          Cours
        </NuxtLink>
        <NuxtLink
          :class="navLinkClasses"
          to="/danses"
        >
          Danses
        </NuxtLink>
        <NuxtLink
          :class="navLinkClasses"
          to="/agenda"
        >
          Agenda
        </NuxtLink>
        <NuxtLink
          :class="navLinkClasses"
          to="/photos"
        >
          Photos
        </NuxtLink>
      </nav>

      <!-- Menu Mobile -->
      <div class="md:hidden">
        <button
          class="focus:outline-none transition-colors"
          :class="
            isHomePage
              ? 'text-white hover:text-secondary-light'
              : 'text-foreground-subtle hover:text-foreground'
          "
          aria-label="Ouvrir le menu"
          @click="toggleMobileMenu"
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
            />
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
            />
          </svg>
        </button>
      </div>

      <!-- Menu Mobile Dropdown -->
      <div
        v-if="isMobileMenuOpen"
        class="absolute top-full left-0 w-full shadow-lg md:hidden"
        :class="
          isHomePage
            ? 'bg-gray-950/90 text-white backdrop-blur-md'
            : 'bg-background text-foreground'
        "
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
defineOptions({ name: "AppHeader" });

const route = useRoute();
const isMobileMenuOpen = ref(false);
const isHomePage = computed(() => route.path === "/");
const navLinkClasses = computed(() => [
  "transition-colors duration-300 font-medium",
  isHomePage.value
    ? "text-white/90 hover:text-secondary-light drop-shadow-sm"
    : "text-foreground-muted hover:text-primary",
]);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>
