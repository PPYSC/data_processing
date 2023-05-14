import torch
from transformers import T5ForConditionalGeneration, RobertaTokenizer

model_path = "PPY039/codet5-small-go_generation_v2"
model_path = "intm/codet5-small-go_generation"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# load model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained(model_path, cache_dir="D:\huggingface_cache")
model = T5ForConditionalGeneration.from_pretrained(model_path, cache_dir="D:\huggingface_cache")

model.to(device)

# 使用模型进行推理
input_text = "package models\n\nimport (\n\t\"github.com/astaxie/beego/orm\"\n)\n\ntype PmpCampaignCreative struct {\n\tId             int    `orm:\"column(id);auto\"`\n\tCampaignId     int    `orm:\"column(campaign_id)\"`\n\tName           string `orm:\"column(name);size(45);null\"`\n\tWidth          int    `orm:\"column(width);null\"`\n\tHeight         int    `orm:\"column(height);null\"`\n\tCreativeUrl    string `orm:\"column(creative_url);size(255);null\"`\n\tCreativeStatus int    `orm:\"column(creative_status);null\"`\n\tLandingUrl     string `orm:\"column(landing_url);size(500);null\"`\n\tImpTrackingUrl string `orm:\"column(imp_tracking_url);size(1000);null\"`\n\tClkTrackingUrl string `orm:\"column(clk_tracking_url);size(1000)\"`\n\tDisplayTitle   string `orm:\"column(display_title);size(200);null\"`\n\tDisplayText    string `orm:\"column(display_text);size(1000);null\"`\n}\n\nfunc (t *PmpCampaignCreative) TableName() string {\n\treturn \"pmp_campaign_creative\"\n}\n\n\n\nfunc AddPmpCampaignCreative(v *PmpCampaignCreative) (err error) {\n\to := orm.NewOrm()\n\n\t_, err = o.Insert(v)\n\treturn err\n\n}\n\nfunc init() "

input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)

output = model.generate(input_ids=input_ids, max_new_tokens=256)  # 最大长度按照数据集的max_trg_len设置

# 将生成的结果转换为字符串
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)
