<script>
import Mirador from 'mirador/dist/es/src/index'
import {miradorImageToolsPlugin} from 'mirador-image-tools'

let miradorInstance

export default {
  async asyncData({$axios}) {
    // 取得先のURL
    const url = 'https://www.dl.ndl.go.jp/api/iiif/1823865/manifest.json'
    // リクエスト（Get）
    const response = await $axios.$get(url)
  },
  data() {
    return {
      canvas: '',
    }
  },

  computed: {
    miradorViewerOptions() {
      return {
        id: 'mirador',
        windows: [
          {
            id: 'known-window-id',
            manifestId: this.manifestId,
          },
        ],
        window: {
          allowClose: false,
          allowMaximize: false,
          allowFullscreen: true,
          hideWindowTitle: true,
        },
        workspaceControlPanel: {
          enabled: false,
        },
      }
    },
  },

  watch: {
    canvas() {
      // We create the action first. Note we are using a specified `windowId` here. This could be accessed from the store instead of specifying upfront.
      const action = Mirador.actions.setCanvas('known-window-id', this.canvas)
      // Now we can dispatch it.
      miradorInstance.store.dispatch(action)
    },
  },

  mounted() {
    miradorInstance = Mirador.viewer(this.miradorViewerOptions, [
      ...miradorImageToolsPlugin,
    ])
  },

  beforeDestroy() {
    miradorInstance.unmount()
  },

  methods: {
    zoom() {
      // Box to zoom to
      const boxToZoom = {
        x: 1420,
        y: 1831,
        width: 800,
        height: 1195,
      }

      const zoomCenter = {
        x: boxToZoom.x + boxToZoom.width / 2,
        y: boxToZoom.y + boxToZoom.height / 2,
      }
      const action = Mirador.actions.updateViewport('known-window-id', {
        x: zoomCenter.x,
        y: zoomCenter.y,
        zoom: 1 / boxToZoom.width,
      })

      miradorInstance.store.dispatch(action)
    },
  },
}
</script>
<template>
  <v-container>
    <h1 class="mb-5">{{ label }}</h1>

    <div class="mb-5">
      <v-select
          v-model="canvas"
          :items="canvases"
          label="Select Canvas"
      ></v-select>
      <v-btn color="primary" @click="zoom">Zoom</v-btn>
      <v-btn color="primary" @click="zoom">表示方向切り替え</v-btn>
    </div>

    <div id="mirador" class="mb-10"></div>
    <v-table>
      <tbody>
      <tr v-for="(item, key) in metadata" :key="key">
        <th>{{ item.label }}</th>
        <td>{{ item.value }}</td>
      </tr>
      </tbody>
    </v-table>
  </v-container>
</template>
<style>
#mirador {
  height: 600px;
  position: relative;
  width: 100%;
}
</style>
