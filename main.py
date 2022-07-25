import argparse
from Text2LIVE import Text2LIVE

def parse_args():
    parser = argparse.ArgumentParser(description='CLIP')
    parser.add_argument("--train", "-t", action="store_true", default=False, help="training")
    parser.add_argument("--inference", "-i", action="store_true", default=False, help="training")
    parser.add_argument("--wandb", "-w", action="store_true", default=False, help="wand loggings")
    parser.add_argument("--save_weight", "-s", action="store_true", default=True, help="save model weight")
    return parser.parse_args()

def main():
    args = parse_args()
    text2live = Text2LIVE(args)

    #build model
    print("build_model")
    text2live.build_model()

    if args.train:
        print("train start")
        text2live.train()

    if args.save_weight:
        text2live.save_weight()

    if args.inference:
        text2live.inference()

if __name__=="__main__":
    main()