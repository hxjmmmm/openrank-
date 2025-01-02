import * as request from '@/utils/request'
/**
 * 接口封装
 */
export default {
    getKddOverall(pojoname) {
        // 使用模板字符串构建包含 pojobName 参数的 URL
        let url = `/api/kdd/sa`;
        return request.get(url);
  }
}