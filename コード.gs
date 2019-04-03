var SHEET_ID = "1h7AU7ayiUQKcX4wZ9xdZthvfEGOs7ESeQ-97nwPHr2Y";
function doGet(e) {
  var today = Utilities.formatDate(new Date(), "JST", "yyyy-MM-dd");
  var sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(today); 
  if(sheet != null){
    // 存在した場合
    //Logger.log("exist");
  }else{
    // 存在しない場合 → シートの作成
    //Logger.log("no");
    var sheet = SpreadsheetApp.openById(SHEET_ID).insertSheet(today);
  }
  // 最終行にテキスト追加
  var LastRow = sheet.getLastRow();
  // 送られてきたtextを取得
  var text = e.parameters.text;
  sheet.getRange(LastRow+1, 1).setValue(text);
}
