// 静态 session 自治

<template>
  <div class="staticsession">
    <SessionTitle v-bind:sessContent="this.sessionContent"></SessionTitle>
    <div class="staticsession-body">
      <!-- <ModelStatic></ModelStatic>
      <DatasetStatic></DatasetStatic>
      <TrainStatic></TrainStatic>
      <SysStatic></SysStatic>
      <MsmgStatic></MsmgStatic>-->

      <!-- swiper 走马灯 https://github.surmon.me/vue-awesome-swiper/  -->
      <md-card>
        <md-card-media>
          <!-- swiper -->
          <swiper :options="swiperOption">
            <swiper-slide>
              <ModelStatic></ModelStatic>
            </swiper-slide>
            <swiper-slide>
              <DatasetStatic></DatasetStatic>
            </swiper-slide>
            <swiper-slide>
              <TrainStatic></TrainStatic>
            </swiper-slide>
            <swiper-slide>
              <SysStatic></SysStatic>
            </swiper-slide>
            <swiper-slide>
              <MsmgStatic></MsmgStatic>
            </swiper-slide>

            <div class="swiper-pagination" slot="pagination"></div>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
        </md-card-media>
      </md-card>
    </div>

    <div class="staticsession-foot">
      <!-- 无内容扩展整体高度 -->
    </div>
  </div>
</template>

<script>
import SessionTitle from "./SessionTitle";
import DatasetStatic from "./staticinfo/DatasetStatic";
import TrainStatic from "./staticinfo/TrainStatic";
import SysStatic from "./staticinfo/SysStatic";
import MsmgStatic from "./staticinfo/MsmgStatic";
import ModelStatic from "./staticinfo/ModelStatic";

export default {
  name: "StaticSession",
  data() {
    return {
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 30,
        freeMode: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },

        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      },

      sessionContent: "静态信息",

    };
  },

  components: {
    SessionTitle,
    DatasetStatic,
    TrainStatic,
    SysStatic,
    MsmgStatic,
    ModelStatic
  }
};
</script>

<style scoped>
.staticsession-body {
  height: auto;
}
.staticsession-foot {
  height: 50px;
}

.datasetstatic {
  display: inline-block;
  /* padding: 8px; */
  /* width: 400px; */
}
.trainstatic {
  display: inline-block;
  /* padding: 8px; */
  /* width: 400px; */
}
.sysstatic {
  display: inline-block;
  /* padding: 8px; */
  /* width: 400px; */
}
.msmgstatic {
  display: inline-block;
  /* padding: 8px; */
  /* width: 400px; */
}
.modelstatic {
  display: inline-block;
  /* padding: 8px; */
  /* width: 400px; */
}
</style>
