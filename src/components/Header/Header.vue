<template>
  <header class="bg-white shadow-md">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <NavLink to="/">
        <div class="text-2xl font-bold text-gray-800">
          DML Country
        </div>
      </NavLink>

      <!-- Navigation Desktop -->
      <nav class="hidden md:flex space-x-6">
        <NavLink to="/cours">Cours</NavLink>
        <NavLink to="/danses">Danses</NavLink>
        <NavLink to="/agenda">Agenda</NavLink>
        <NavLink to="/instagram">Instagram</NavLink>
      </nav>

      <!-- Menu Mobile -->
      <div class="md:hidden">
        <button @click="toggleMobileMenu" class="text-gray-600 hover:text-gray-800 focus:outline-none">
          <svg v-if="!isMobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>

      <!-- Menu Mobile Dropdown -->
      <div v-if="isMobileMenuOpen" class="absolute top-16 left-0 w-full bg-white shadow-lg md:hidden">
        <nav class="flex flex-col p-4 space-y-2">
          <NavLink to="/cours" @click="toggleMobileMenu">Cours</NavLink>
          <NavLink to="/danses" @click="toggleMobileMenu">Danses</NavLink>
          <NavLink to="/agenda" @click="toggleMobileMenu">Agenda</NavLink>
          <NavLink to="/instagram" @click="toggleMobileMenu">Instagram</NavLink>
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import NavLink from "./NavLink"

const isMobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}
</script>