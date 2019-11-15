<template>
  <div class="search">
    <el-row :gutter="20">
      <el-col :span="6">
        <div class="grid-content bg-purple">
          <center> <label style="line-height: 178px;">点击上传图片：</label></center>

        </div>
      </el-col>
      <el-col :span="12">
        <div class="demo-shadow" style="padding: 5px;box-shadow: rgba(0, 0, 0, 0.12) 0px 2px 4px, rgba(0, 0, 0, 0.04) 0px 0px 6px;">
          <center>
            <div class="grid-content bg-purple">
              <el-upload
                class="avatar-uploader"
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-upload>
            </div>
          </center>
        </div>

      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple" style="line-height: 178px">
          <center>
            <el-button type="primary" icon="el-icon-search">搜索</el-button>
          </center>
        </div>
      </el-col>
    </el-row>

    <ul class="picC">
      <li><img v-for="url in urls" :src="url" alt="" /></li>
    </ul>
    
  </div>
</template>

<script>
export default {
    name: 'SearchView',
    data () {
        return {
            imageUrl: '',
            url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
            urls: [
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
                'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
                'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
            ]
        }
    },
    methods: {
        handleAvatarSuccess(res, file)
        {
            this.imageUrl = URL.createObjectURL(file.raw);
        },
        beforeAvatarUpload(file) {
            return true;
        }
    }
}
</script>

<style scoped>
  .search{
    margin: 20px;
  }

</style>
<style>
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    /*width: 178px;*/
    min-width: 70px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    min-width: 70px;
    height: 178px;
    display: block;
  }
  image{
    width: auto;
    height: 100%;
  }

  img{
    width:100%;
  }


  .picC{
    width:90%;
    -webkit-column-count:4;
    -moz-column-count:4;
    column-count:4;
    -webkit-column-gap:10px;
    -moz-column-gap:10px;
    -column-gap:10px;
    list-style:none;
  }
  /*.picC li{*/
  /*  !*margin-top:20px;*!*/
  /*  !*padding: 10px;*!*/
  /*}*/

</style>
