REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (1, 'zh_TW', '{WEB_TITLE} - 有訪客對你的清單發表了回應', '<p>{CONTACT_NAME} 你好；</p><p>{USER_NAME} ({USER_EMAIL}, {USER_PHONE}) 在你的清單中發表了訊息：<a href="{ITEM_URL}">{ITEM_TITLE}</a>:</p><p>{COMMENT}</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (2, 'zh_TW', '請驗證你的 {WEB_TITLE} 帳號', '<p>{USER_NAME} 你好；</p><p>請驗證你的註冊是否為你本人，請按一下右側超連結：{VALIDATION_LINK}</p><p>謝謝你！</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (3, 'zh_TW', '{WEB_TITLE} - 註冊成功！', '<p>你好； {USER_NAME},</p><p>閣下已成功登記成我們會員 {WEB_LINK}.</p><p>謝謝!</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (4, 'zh_TW', '看看我在 {WEB_TITLE} 發現了什麼', '<p>{FRIEND_NAME} 你好；</p><p>你的朋友 {USER_NAME} 分享這個廣告清單給你 <a href="{ITEM_URL}">{ITEM_TITLE}</a>.</p><p>內容：</p><p>{COMMENT}</p><p>祝好</p><p>{WEB_TITLE}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (5, 'zh_TW', '{WEB_TITLE} - 最近一個小時發佈的新清單 ', '<p>{USER_NAME} 你好；</p><p>最近一個小時發佈的新清單，去瞧一瞧吧！</p><p>{ADS}</p><p>-------------</p><p>若不想訂閱這類通知，請按一下右側超連結：{UNSUB_LINK}</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (6, 'zh_TW', '{WEB_TITLE} - 最近一天發佈的新清單', '<p>{USER_NAME} 你好；</p><p>最近一天發佈的新清單，去瞧一瞧吧！</p><p>{ADS}</p><p>-------------</p><p>若不想訂閱這類通知，請按一下右側超連結：{UNSUB_LINK}</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (7, 'zh_TW', '{WEB_TITLE} - 最近一週發佈的新清單', '<p>{USER_NAME} 你好；</p><p>最近一週發佈的新清單，去瞧一瞧吧！</p><p>{ADS}</p><p>-------------</p><p>若不想訂閱這類通知，請按一下右側超連結：{UNSUB_LINK}</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (8, 'zh_TW', '{WEB_TITLE} - 新清單', '<p>{USER_NAME} 你好；</p><p>有新的清單發佈，請查看！</p><p>{ADS}</p><p>-------------</p><p>若不想訂閱這類通知，請按一下右側超連結：{UNSUB_LINK}</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (9, 'zh_TW', '{WEB_TITLE} - 新的線上留言', '<p>有人在你的廣告清單中留言 <a href="{ITEM_URL}">{ITEM_TITLE}</a>.</p><p>發佈者: {COMMENT_AUTHOR}<br />發佈者電郵地址: {COMMENT_EMAIL}<br />標題: {COMMENT_TITLE}<br />內容: {COMMENT_TEXT}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (10, 'zh_TW', '{WEB_TITLE} - 編輯清單的功能選項 {ITEM_TITLE}', '<p>你好 {USER_NAME},</p><p>雖然閣下還未登記成我們會員 {WEB_LINK}，閣下也能在短期內直接編輯或刪除你的廣告清單 <a href="{ITEM_URL}">{ITEM_TITLE}</a> </p><p>請按一下右側超連結去編輯你的廣告清單: {EDIT_LINK}</p><p>請按一下右側超連結去刪除你的廣告清單: {DELETE_LINK}</p><p>閣下在登記為會員後可以完全管理已發佈的廣告清單.</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (11, 'zh_TW', '{WEB_TITLE} - 驗證你的廣告清單', '<p>你好 {USER_NAME},</p><p>這封電郵是通知閣下剛發佈的廣告: {WEB_LINK}. 請按一下右側超連結驗證你的廣告清單: {VALIDATION_LINK}. 如果閣下沒有發佈新的廣告，請不用理會這郵件.</p><p>詳細資料:</p><p>聯絡人: {USER_NAME}<br />聯絡人電郵地址: {USER_EMAIL}</p><p>{ITEM_DESCRIPTION}</p><p>超連接: <a href="{ITEM_URL}">{ITEM_TITLE}</a></p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (12, 'zh_TW', '{WEB_TITLE} - 有新的廣告清單發佈', '<p>你好 {WEB_TITLE} admin,</p><p>這封電郵是通知閣下剛發佈的廣告: {WEB_LINK}.</p><p>詳細資料:</p><p>聯絡人: {USER_NAME}<br />聯絡人電郵地址: {USER_EMAIL}</p><p>{ITEM_DESCRIPTION}</p><p>超連接: <a href="{ITEM_URL}">{ITEM_TITLE}</a></p><p>請按一下右側超連結去編輯你的廣告清單: {EDIT_LINK}</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (13, 'zh_TW', '{WEB_TITLE} - 找回你的密碼', '<p>你好 {USER_NAME},</p><p>閣下向我們要求了戶口密碼提示. 請按一下右側超連結去開始: {PASSWORD_LINK}</p><p>這超連結只在未來24小時有效.</p><p>如果閣下沒有向我們要求了戶口密碼提示, 請不用理會這郵件. 核對發出查詢的IP地址 {IP_ADDRESS} 和時間 {DATE_TIME}</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (14, 'zh_TW', '{WEB_TITLE} - 你要求變更電子郵件', '<p>你好 {USER_NAME}</p><p>閣下向我們要求了電郵地址更新. 請按一下右側超連結去開始確認程序: {VALIDATION_LINK}</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (15, 'zh_TW', '{WEB_TITLE} - 請驗證你的通知功能', '<p>{USER_NAME} 你好；</p><p>你開啟通知功能，須驗證後啟用，請按一下右側超連結：{VALIDATION_LINK}</p><p>謝謝！</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (16, 'zh_TW', '{WEB_TITLE} - 你的線上留言已經核准', '<p>{COMMENT_AUTHOR} 你好；</p><p>你在 <a href="{ITEM_URL}">{ITEM_TITLE}</a> 發表的線上留言已經核准。</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (17, 'zh_TW', '{WEB_TITLE} - 驗證你的廣告清單', '<p>你好 {USER_NAME},</p><p>這封電郵是通知閣下剛發佈的廣告: {WEB_LINK}. 請按一下右側超連結驗證你的廣告清單: {VALIDATION_LINK}. 如果閣下沒有發佈新的廣告，請不用理會這郵件.</p><p>詳細資料:</p><p>聯絡人: {USER_NAME}<br />聯絡人電郵地址: {USER_EMAIL}</p><p>{ITEM_DESCRIPTION}</p><p>超連接: <a href="{ITEM_URL}">{ITEM_TITLE}</a></p><p>即使沒有登記成我們會員，閣下也能編輯你的廣告清單{WEB_LINK}:</p><p>請按一下右側超連結去編輯你的廣告清單: {EDIT_LINK}</p><p>請按一下右側超連結去刪除你的廣告清單: {DELETE_LINK}</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (18, 'zh_TW', '{WEB_TITLE} - 有新的使用者註冊', '<p>你好 {WEB_TITLE} admin,</p><p>有新加入會員 {WEB_LINK}.</p><p>詳細資料:</p><p>用戶名: {USER_NAME}<br />電郵地址: {USER_EMAIL}</p><p>祝好,</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (19, 'zh_TW', '{WEB_TITLE} - 有人留言給你', '<p>{CONTACT_NAME} 你好；</p><p>{USER_NAME} ({USER_EMAIL}, {USER_PHONE}) 留言給你：</p><p>{COMMENT}</p><p>祝好</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (20, 'zh_TW', '{WEB_TITLE} - 有人在你的廣告清單中留言', '<p>你好, 有人在你的廣告清單中留言: <a href="{ITEM_URL}">{ITEM_TITLE}</a>.</p><p>發佈者: {COMMENT_AUTHOR}<br />發佈者電郵地址 {COMMENT_EMAIL}<br />標題: {COMMENT_TITLE}<br />內容: {COMMENT_TEXT}</p><p>{WEB_LINK}</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (21, 'zh_TW', '{WEB_TITLE} - 成功建立管理員帳號！', '<p>你好 {ADMIN_NAME}，</p><p>{WEB_LINK} 的管理員已經為你建立帳號，</p><ul><li>使用者名稱：{USERNAME}</li><li>密碼： {PASSWORD}</li></ul><p>你可以進入管理員控制面板，請按一下 {WEB_ADMIN_LINK}。</p><p>謝謝！</p><p>祝好，</p>');
REPLACE INTO /*TABLE_PREFIX*/t_pages_description (fk_i_pages_id, fk_c_locale_code, s_title, s_text) VALUES (22, 'zh_TW', '{WEB_TITLE} - 你的廣告快要到期', '<p>你好 {USER_NAME}，</p><p>你在 {WEB_LINK} 的廣告 <a href="{ITEM_URL}">{ITEM_TITLE}</a> 已經快要到期。');

