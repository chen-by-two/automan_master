import allure

import ApiLib.stagnation.stagnationApi as stagnation


class Test_stagnation:

	@allure.feature("stagnation")
	@allure.severity("normal")
	def test_StagnationUserStatistic_testConn(self):
		"""
		个人中心数据统计
		"""
		StagnationUserStatistic=stagnation.StagnationUserStatistic()
		StagnationUserStatistic.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjcxODcsInd4T3BlbmlkIjoib2YtRlh3NXVLWU1oV0x4NFJWN3lNX3B4SVRmcyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjcxODciLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU4MDk2XHU2NTg3XHU3NDc2IiwibW9iaWxlIjoiMTU2NTE3MTE3MjkifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.rabiKn7QQ4451LNO3y2LoI2NOzsPthsPYRb-Hz2t_xMO7FiW0S4pOaG7x-KTvkTd67jCJ4OMfV9A0UP4P7DOtkj1zjO7UkHB8SItrft2LlFrLJacSzgtstMATBgy0VfEuU3we49vA-CwKU_qf3QNKlFAQP9wd_T7mAIhIhEh6pMM0Ui-HwvbJ7TmOWvKMA-IV1HI_1Hm7YPvFlfwkmXt10YAsBN9QTm6WaWeCgTnJ8bYZu77xISeYqumprnFOb6lOTtT0k30oO_t6Mrs8eT4OfeEaDCmC9iv5qH614lPJ_Ad4WJcE0S5SQwi8NM3NVE-zIv97IYA3VB4KZBXLdQ0Pw"}
		StagnationUserStatistic.changeEnv("turboradio.cn")
		StagnationUserStatistic.data = {"memberId": "15967187"}
		StagnationUserStatisticRes = StagnationUserStatistic.excute()
		assert StagnationUserStatisticRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("stagnation")
	@allure.severity("normal")
	def test_StagnationUserRecordPaging_testConn(self):
		"""
		发放记录查询
		"""
		StagnationUserRecordPaging=stagnation.StagnationUserRecordPaging()
		StagnationUserRecordPaging.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjcxODcsInd4T3BlbmlkIjoib2YtRlh3NXVLWU1oV0x4NFJWN3lNX3B4SVRmcyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjcxODciLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU4MDk2XHU2NTg3XHU3NDc2IiwibW9iaWxlIjoiMTU2NTE3MTE3MjkifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.rabiKn7QQ4451LNO3y2LoI2NOzsPthsPYRb-Hz2t_xMO7FiW0S4pOaG7x-KTvkTd67jCJ4OMfV9A0UP4P7DOtkj1zjO7UkHB8SItrft2LlFrLJacSzgtstMATBgy0VfEuU3we49vA-CwKU_qf3QNKlFAQP9wd_T7mAIhIhEh6pMM0Ui-HwvbJ7TmOWvKMA-IV1HI_1Hm7YPvFlfwkmXt10YAsBN9QTm6WaWeCgTnJ8bYZu77xISeYqumprnFOb6lOTtT0k30oO_t6Mrs8eT4OfeEaDCmC9iv5qH614lPJ_Ad4WJcE0S5SQwi8NM3NVE-zIv97IYA3VB4KZBXLdQ0Pw"}
		StagnationUserRecordPaging.changeEnv("turboradio.cn")
		StagnationUserRecordPaging.data = {"memberId": "15967187","date": "","status": "1","equityNo": "","note": "","page": "1","limit": "10"}
		StagnationUserRecordPagingRes = StagnationUserRecordPaging.excute()
		assert StagnationUserRecordPagingRes.text.__contains__("\"errno\":\"0\"")
import ApiLib.stagnation.stagnationApi as stagnation


class Test_stagnation:

	@allure.feature("stagnation")
	@allure.severity("normal")
	def test_StagnationUserStatistic_testConn(self):
		"""
		个人中心数据统计
		"""
		StagnationUserStatistic=stagnation.StagnationUserStatistic()
		StagnationUserStatistic.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjcxODcsInd4T3BlbmlkIjoib2YtRlh3NXVLWU1oV0x4NFJWN3lNX3B4SVRmcyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjcxODciLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU4MDk2XHU2NTg3XHU3NDc2IiwibW9iaWxlIjoiMTU2NTE3MTE3MjkifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.rabiKn7QQ4451LNO3y2LoI2NOzsPthsPYRb-Hz2t_xMO7FiW0S4pOaG7x-KTvkTd67jCJ4OMfV9A0UP4P7DOtkj1zjO7UkHB8SItrft2LlFrLJacSzgtstMATBgy0VfEuU3we49vA-CwKU_qf3QNKlFAQP9wd_T7mAIhIhEh6pMM0Ui-HwvbJ7TmOWvKMA-IV1HI_1Hm7YPvFlfwkmXt10YAsBN9QTm6WaWeCgTnJ8bYZu77xISeYqumprnFOb6lOTtT0k30oO_t6Mrs8eT4OfeEaDCmC9iv5qH614lPJ_Ad4WJcE0S5SQwi8NM3NVE-zIv97IYA3VB4KZBXLdQ0Pw"}
		StagnationUserStatistic.changeEnv("turboradio.cn")
		StagnationUserStatistic.data = {"memberId": "15967187"}
		StagnationUserStatisticRes = StagnationUserStatistic.excute()
		assert StagnationUserStatisticRes.text.__contains__("\"errno\":\"0\"")

	@allure.feature("stagnation")
	@allure.severity("normal")
	def test_StagnationUserRecordPaging_testConn(self):
		"""
		发放记录查询
		"""
		StagnationUserRecordPaging=stagnation.StagnationUserRecordPaging()
		StagnationUserRecordPaging.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJJZCI6MTU5NjcxODcsInd4T3BlbmlkIjoib2YtRlh3NXVLWU1oV0x4NFJWN3lNX3B4SVRmcyIsInZlcnNpb24iOnsia2V5IjoiQVVUSF9tb2JpbGVfMTU5NjcxODciLCJ2YWx1ZSI6IjEifSwiaW5mbyI6eyJuYW1lIjoiXHU4MDk2XHU2NTg3XHU3NDc2IiwibW9iaWxlIjoiMTU2NTE3MTE3MjkifSwiY2hhbm5lbCI6eyJ0eXBlIjoibW9iaWxlIn19.rabiKn7QQ4451LNO3y2LoI2NOzsPthsPYRb-Hz2t_xMO7FiW0S4pOaG7x-KTvkTd67jCJ4OMfV9A0UP4P7DOtkj1zjO7UkHB8SItrft2LlFrLJacSzgtstMATBgy0VfEuU3we49vA-CwKU_qf3QNKlFAQP9wd_T7mAIhIhEh6pMM0Ui-HwvbJ7TmOWvKMA-IV1HI_1Hm7YPvFlfwkmXt10YAsBN9QTm6WaWeCgTnJ8bYZu77xISeYqumprnFOb6lOTtT0k30oO_t6Mrs8eT4OfeEaDCmC9iv5qH614lPJ_Ad4WJcE0S5SQwi8NM3NVE-zIv97IYA3VB4KZBXLdQ0Pw"}
		StagnationUserRecordPaging.changeEnv("turboradio.cn")
		StagnationUserRecordPaging.data = {"memberId": "15967187","date": "","status": "1","equityNo": "","note": "","page": "1","limit": "10"}
		StagnationUserRecordPagingRes = StagnationUserRecordPaging.excute()
		assert StagnationUserRecordPagingRes.text.__contains__("\"errno\":\"0\"")
