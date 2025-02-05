<script>
import "tify";
import "tify/dist/tify.css";
export default {
  mounted() {
    new Tify({
      container: "#tify",
      manifestUrl: "https://www.dl.ndl.go.jp/api/iiif/1823865/manifest.json",
    });
  },
};
</script>
<template>
  <div id="tify" style="height: 640px"></div>
</template>
