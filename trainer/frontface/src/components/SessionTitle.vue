// 章节头

<template>
    <div class="sessiontitle">
        <hr class="sess-hr" />
        <p class="sess-p">
            {{ sessContent }}
        </p>
    </div>
</template>

<script>
export default {
    name : "SessionTitle",

    props : ["sessContent"],

    data() {
        return {
            
        }
    },

    methods: {
        
    },

}
</script>

<style scoped>
.sessiontitle{
    text-align:left;
};
.sess-p {
    text-align:"left";
    font-size:40px;
    color:"red";
};
.sess-hr {
    height:0.5px;
    border:none;
    border-top:1px solid #555555;
}

</style>

