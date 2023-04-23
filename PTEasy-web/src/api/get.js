import HTTP from '@/utils/request'

export default {
    logsList(data) {
        return HTTP.get('/v1/logs/list', {params: data});
    },
    taskList(data) {
        return HTTP.get('/v1/task/list', {params: data});
    }
}