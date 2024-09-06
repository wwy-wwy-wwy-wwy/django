// JavaScript Document
function f1()
{
	alert("恭喜你成功设为首页！");
}
function f2()
{
	alert("恭喜你成功加入收藏！");
}


// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option = {
  xAxis: {
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {},
  series: [
    {
      type: 'bar',
      data: [23, 24, 18, 25, 27, 28, 25]
    }
  ]
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);