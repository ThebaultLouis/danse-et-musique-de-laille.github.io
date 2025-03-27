<template>
  <nuxt-link 
    :to="to" 
    class="text-gray-700 hover:text-blue-600 transition-colors duration-300 font-medium"
  >
    <slot>
      Lien
    </slot>
  </nuxt-link>
</template>

<script setup>
defineProps({
  to: {
    type: String,
    required: true
  }
})

</script>