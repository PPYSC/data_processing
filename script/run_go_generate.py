import torch

from go_generate.go_generator import GoGenerator

MODEL_PATH = "PPY039/codet5-small-go_generation_v2"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CACHE_DIR = "D:\huggingface_cache"

go_generator = GoGenerator(MODEL_PATH, DEVICE, CACHE_DIR)

input_text = "package models\n\nimport (\n\t\"github.com/astaxie/beego/orm\"\n)\n\ntype PmpCampaignCreative struct {\n\tId             int    `orm:\"column(id);auto\"`\n\tCampaignId     int    `orm:\"column(campaign_id)\"`\n\tName           string `orm:\"column(name);size(45);null\"`\n\tWidth          int    `orm:\"column(width);null\"`\n\tHeight         int    `orm:\"column(height);null\"`\n\tCreativeUrl    string `orm:\"column(creative_url);size(255);null\"`\n\tCreativeStatus int    `orm:\"column(creative_status);null\"`\n\tLandingUrl     string `orm:\"column(landing_url);size(500);null\"`\n\tImpTrackingUrl string `orm:\"column(imp_tracking_url);size(1000);null\"`\n\tClkTrackingUrl string `orm:\"column(clk_tracking_url);size(1000)\"`\n\tDisplayTitle   string `orm:\"column(display_title);size(200);null\"`\n\tDisplayText    string `orm:\"column(display_text);size(1000);null\"`\n}\n\nfunc (t *PmpCampaignCreative) TableName() string {\n\treturn \"pmp_campaign_creative\"\n}\n\n\n\nfunc AddPmpCampaignCreative(v *PmpCampaignCreative) (err error) {\n\to := orm.NewOrm()\n\n\t_, err = o.Insert(v)\n\treturn err\n\n}\n\nfunc init() "

print(go_generator.generate(input_text))