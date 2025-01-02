<template>
  <div ref="rateChart" style="width: 500%; height: 100%"></div>
</template>
<script>
let chart = null
export default {
  props: {
    title: String,
    data: Object,
  },
  data () {
    return {
      d: 1111
    }
  },
  methods: {
    initChart () {
   
    },
    setOptions() {
      
    }
  },
  watch: {
    data: {
     
    }
  }
}
</script>