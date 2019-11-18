<template>
  <div id="app">
    <el-header>
      <el-menu default-active="1"
               class="el-menu-demo"
               mode="horizontal"
               background-color="#545c64"
               text-color="#fff"
               active-text-color="#ffd04b">
        <el-menu-item index="1">MMFinder Web Demo</el-menu-item>
      </el-menu>
    </el-header>
    <SearchView/>
  </div>
</template>

<script>
import SearchView from './components/SearchView'

export default {
  name: 'App',
  components: {
      SearchView
  }
}
</script>

<style>
  .el-header {
    padding: 0!important;
  }
  body{
    margin: 0;
  }
</style>

