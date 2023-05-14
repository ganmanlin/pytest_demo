import allure


@allure.description("""
多行描述语：<br/>
这是通过传递字符串参数的方式添加的一段描述语，<br/>
使用的是装饰器 @allure.description
""")
def test_description_provide_string():
    assert True


@allure.description_html(
    """<form id="form" name="f" action="/s" class="fm  has-soutu has-voice"><div class="bdsug bdsug-new new-pmd bdsugbg" style="height: auto; display: none;"><ul><li data-key="pytest hook函数" class="bdsug-store bdsug-overflow c-line-clamp1"><span>pytest hook函数</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="pytest-xdist" class="bdsug-store bdsug-overflow c-line-clamp1"><span>pytest-xdist</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="mac openpyxl 打开excel提示找不到文件" class="bdsug-store bdsug-overflow c-line-clamp1"><span>mac openpyxl 打开excel提示找不到文件</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="openpyxl 打开excel提示找不到文件" class="bdsug-store bdsug-overflow c-line-clamp1"><span>openpyxl 打开excel提示找不到文件</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="pytest.raise() 例子" class="bdsug-store bdsug-overflow c-line-clamp1"><span>pytest.raise() 例子</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="pytest.raise()" class="bdsug-store bdsug-overflow c-line-clamp1"><span>pytest.raise()</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="谷歌开源风格指南" class="bdsug-store bdsug-overflow c-line-clamp1"><span>谷歌开源风格指南</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="dbvisualizer使用教程" class="bdsug-store bdsug-overflow c-line-clamp1"><span>dbvisualizer使用教程</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li><li data-key="dbvear" class="bdsug-store bdsug-overflow c-line-clamp1"><span>dbvear</span><u class="bdsug-store-del " title="如您不需要此搜索历史提示，
可在右上角搜索设置中关闭">删除</u></li></ul><div style="text-align:right; background:none; height: 25px; line-height: 15px; border-radius: 0 0 10px 10px;padding-bottom: 2px;margin-top: -5px;"><span class="setup_storeSug" style="margin-right:12px; text-decoration:none; cursor:pointer;font-size: 13px; color: #9195a3">关闭历史</span></div></div><input type="hidden" name="ie" value="utf-8"><input type="hidden" name="f" value="8"><input type="hidden" name="rsv_bp" value="1"><input type="hidden" name="rsv_idx" value="1"><input type="hidden" name="ch" value=""><input type="hidden" name="tn" value="baidu"><input type="hidden" name="bar" value=""><span class="bg s_ipt_wr new-pmd quickdelete-wrap"><span class="ipt_rec" style="display: block;"></span><span class="soutu-btn"></span><input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off"><i class="c-icon quickdelete c-color-gray2" title="清空" style="display: none;"></i><i class="quickdelete-line" style="display: none;"></i><span class="soutu-hover-tip" style="display: none;">按图片搜索</span><span class="voice-hover" style="display: none;">按语音搜索</span></span><span class="bg s_btn_wr"><input type="submit" id="su" value="百度一下" class="bg s_btn"></span><span class="tools"><span id="mHolder"><div id="mCon"><span>
                                    输入法</span></div><ul id="mMenu"><li><a href="javascript:;" name="ime_hw">
                                    手写</a></li><li><a href="javascript:;" name="ime_py">
                                    拼音</a></li><li class="ln"></li><li><a href="javascript:;" name="ime_cl">
                                    关闭</a></li></ul></span></span><input type="hidden" name="rn" value=""><input type="hidden" name="fenlei" value="256"><input type="hidden" name="oq" value=""><input type="hidden" name="rsv_pq" value="0x8932cc49000001a5"><input type="hidden" name="rsv_t" value="c988gwGh3Z2YPFlR4rWwIhRFOR/ASFmNf6m30eBqKJhaTvXFoSXGFzbiLvxC"><input type="hidden" name="rqlang" value="en"><input type="hidden" name="rsv_enter" value="1"><input type="hidden" name="rsv_dl" value="ib"><input type="hidden" name="rsv_sug3" value="1"><input type="hidden" name="rsv_sug1" value="1"><input type="hidden" name="rsv_sug7" value="001"></form>""")
def test_description_privide_html():
    assert True


def test_description_docstring():
    """
    直接在测试用例方法中
    通过编写文档注释的方法
    来添加描述。
    :return:
    """
    assert True


@allure.description("""这个描述将被替换""")
def test_dynamic_description():
    assert 42 == int(6 * 7)
    allure.dynamic.description('这是最终的描述信息')
    # allure.dynamic.description_html(''' html 代码块 ''')
