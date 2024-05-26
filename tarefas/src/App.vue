<script>
export default {
    name: 'App',
    mounted() {
      document.getElementById('app').style = 'min-height: ' + (window.innerHeight-195) + 'px'
    }
}
</script>

<template>
    <router-view></router-view>
</template>

<style scoped>

</style>
