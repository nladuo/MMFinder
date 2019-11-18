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
                  action="/api/upload_image"
                  name="file"
                  :show-file-list="false"
                  :on-success="handleAvatarSuccess">
                  <img v-if="image_to_search" :src="image_to_search" class="avatar">
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                </el-upload>
                <img v-if="face_to_search" :src="face_to_search" class="face_to_search">
            </div>
          </center>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="grid-content bg-purple" style="line-height: 178px">
          <center>
            <el-button type="primary" icon="el-icon-search" @click="searchImage">搜索</el-button>
          </center>
        </div>
      </el-col>
    </el-row>

    <ul class="result_pic_list">
      <li><img v-for="url in result_imgs" :src="url" alt="" /></li>
    </ul>

  </div>
</template>

<script>
    import Api from "../actions/api"
    export default {
        name: 'SearchView',
        data () {
            return {
                image_to_search: '',
                search_param: "",
                result_imgs: [],
                face_to_search: ""
            }
        },
        mounted() {
            // this.searchImage()
        },
        methods: {
            handleAvatarSuccess(res, file)
            {
                console.log(res);
                if (res.success){
                    this.$message({
                        message: '上传成功',
                        type: 'success'
                    });
                    this.search_param = res.filename;
                    this.face_to_search = "/api/get_upload_images/face-" + res.filename;
                    this.image_to_search = URL.createObjectURL(file.raw);
                } else {
                    this.search_param = "";
                    this.image_to_search = "";
                    this.face_to_search = "";
                    this.$message.error(res.msg);
                }
            },
            searchImage() {
                this.result_imgs = [];
                const loading = this.$loading({
                    lock: true,
                    text: 'Loading',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.7)'
                });

                Api.get("/search", {
                    "filename": this.search_param
                }, (data)=>{
                    loading.close();
                    console.log(data);
                    if (data.success) {
                        data.data.forEach((elem)=>{
                            this.result_imgs.push("/api/get_images/" + elem)
                        });
                    } else {
                        this.$message.error(data.msg);
                    }
                })
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
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: auto;
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

.face_to_search{
  width: 40px;
  height: 40px;
}

.result_pic_list{
  width:90%;
  -webkit-column-count:5;
  -moz-column-count:5;
  column-count:5;
  -webkit-column-gap:10px;
  -moz-column-gap:10px;
  -column-gap:10px;
  list-style:none;
}
</style>
