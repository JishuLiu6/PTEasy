<template>
    <div id="home">
        <div id="server-list">
            <div class="server-list-item">
                <el-image :src="$imgUrl('pteasy_logo.png')" class="server-list-img"></el-image>
                <div class="server-list-item-info">
                    <div class="connect-icon"></div>
                    <span>PtEasy</span>
                </div>
            </div>
            <div class="server-list-item">
                <el-image :src="$imgUrl('qb.jpeg')" class="server-list-img"></el-image>
                <div class="server-list-item-info">
                    <div class="connect-icon"></div>
                    <span>下载:1</span>
                    <span>保种:100</span>
                </div>
            </div>
            <div class="server-list-item">
                <el-image :src="$imgUrl('utorrent.jpeg')" class="server-list-img"></el-image>
                <div class="server-list-item-info">
                    <div class="connect-icon"></div>
                    <span>下载:1</span>
                    <span>保种:100</span>
                </div>
            </div>
        </div>
        <div id="home-content">
            <el-table id="torrent-table" :data="tableData" border>
                <el-table-column type="expand">
                    <template #default="props">
                        <div>
                            <el-table :data="props.row.torrent_list">
                                <el-table-column fixed="left" label="种子" prop="torrent_name" width="200" />
                                <el-table-column label="大小" prop="size" width="100" />
                                <el-table-column label="标签" width="100">
                                    <template #default="props">
                                        <el-tag type="primary">{{ props.row.tag }}</el-tag>
                                    </template>
                                </el-table-column>
                                <el-table-column label="保种状态" width="100">
                                    <template #default="props">
                                        <el-tag type="success">{{ props.row.state.join('、') }}</el-tag>
                                    </template>
                                </el-table-column>

                                <el-table-column label="文件位置" prop="file_path" />
                                <el-table-column fixed="right" label="操作" width="150">
                                    <template #default="props">
                                        <el-button size="small">编辑</el-button>
                                        <el-button type="danger" size="small">删除</el-button>
                                    </template>
                                </el-table-column>
                            </el-table>
                        </div>
                    </template>
                </el-table-column>
                <el-table-column label="种子文件夹" prop="torrent_path" />
                <el-table-column label="保种/种子">
                    <template #default="props">
                        <el-tag type="success">{{ props.row.torrent_state.seed }}</el-tag>/
                        <el-tag type="warning">{{ props.row.torrent_state.torrent }}</el-tag>
                    </template>
                </el-table-column>
                <el-table-column align="right">
                    <template #header>
                        <el-button type="primary">添加种子文件夹</el-button>
                    </template>
                    <template #default="scope">
                        <el-button size="small">编辑</el-button>
                        <el-button size="small" type="danger">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script setup>
import { getCurrentInstance } from 'vue'
const { proxy } = getCurrentInstance();
const { $imgUrl } = proxy;

const tableData = [
    {
        torrent_path: 'E:\\',
        torrent_state: {
            seed: 1,
            torrent: 1,
        },
        torrent_list: [{
            torrent_name: 'Return.Of.The.Condor.Heroes.S01.2160p.WEB-DL.VP9.AAC-HHWEB',
            tag: '影视',
            size: '200GB',
            file_path: 'E:\\Return.Of.The.Condor.Heroes.S01.2160p.WEB-DL.VP9.AAC-HHWEB',
            state: ['QB'],
        }]
    }
]
</script>
<style scoped>
#server-list {
    margin-top: 20px;
    display: flex;
}

.server-list-item {
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 50px;
}

.connect-icon {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #00ff00;
    margin-right: 5px;
}

.server-list-item-info {
    display: flex;
    /* display: inline-block; */
    align-items: center;
    justify-content: center;
    overflow: hidden;
    min-width: 84px;
    padding: 0 10px;
    font-size: 12px;
    height: 24px;
    line-height: 24px;
    margin: 10px auto;
    border-radius: 24px;
    color: white;
    background: #2065ac;
}

.server-list-item-info>span {
    margin-right: 3px;
    opacity: .5;
}

.server-list-item-info>span:hover {
    opacity: 1;
}

.server-list-img {
    width: 100px;
    height: 100px;
}

#home {
    width: 1160px;
    margin: 0 auto;
}

#home-content {
    width: 1160px;
    height: 60vh;
    background: #fff;
    border-radius: 10px;
    margin-top: 20px;
    padding-top: 20px;
}

#torrent-table {
    width: 80%;
    margin: 0 auto;
}

#server-add {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100px;
    height: 100px;
    border: 1px dashed #989898;
    border-radius: 10px;
    margin-right: 50px;
    background: white;
}
</style>