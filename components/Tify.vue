<script>
import "tify";
import "tify/dist/tify.css";
export default {
  mounted() {
    new Tify({
      container: "#tify",
      manifestUrl: "https://www.dl.ndl.go.jp/api/iiif/1823865/manifest.json",
    });
    // tify.setPage(5);
  },
};
</script>
<template>
  <div id="tify" style="height: 80vh"></div>
</template>
