import torch 
import torch.nn as nn
import torch.nn.functional as F


def ConvBlock(in_channels, out_channels, pool=False):
    layers = [nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
             nn.BatchNorm2d(out_channels),
             nn.ReLU(inplace=True)]
    if pool:
        layers.append(nn.MaxPool2d(4))
    return nn.Sequential(*layers)


# Model Architecture
class ResNet9(nn.Module):
    """
    A custom implementation of the ResNet9 architecture for image classification.
    Args:
        in_channels (int): Number of input channels in the input image.
        num_diseases (int): Number of output classes for classification.
    Attributes:
        conv1 (ConvBlock): First convolutional block.
        conv2 (ConvBlock): Second convolutional block with pooling.
        res1 (nn.Sequential): First residual block consisting of two convolutional blocks.
        conv3 (ConvBlock): Third convolutional block with pooling.
        conv4 (ConvBlock): Fourth convolutional block with pooling.
        res2 (nn.Sequential): Second residual block consisting of two convolutional blocks.
        classifier (nn.Sequential): Classifier block consisting of max pooling, flattening, and a linear layer.
    Methods:
        forward(xb):
            Defines the forward pass of the network.
            Args:
                xb (torch.Tensor): Input batch of images.
            Returns:
                torch.Tensor: Output predictions for the input batch.
    """
    def __init__(self, in_channels, num_diseases):
        super().__init__()
        
        self.conv1 = ConvBlock(in_channels, 64)
        self.conv2 = ConvBlock(64, 128, pool=True) # out_dim : 128 x 64 x 64 
        self.res1 = nn.Sequential(ConvBlock(128, 128), ConvBlock(128, 128))
        
        self.conv3 = ConvBlock(128, 256, pool=True) # out_dim : 256 x 16 x 16
        self.conv4 = ConvBlock(256, 512, pool=True) # out_dim : 512 x 4 x 44
        self.res2 = nn.Sequential(ConvBlock(512, 512), ConvBlock(512, 512))
        
        self.classifier = nn.Sequential(nn.MaxPool2d(4),
                                       nn.Flatten(),
                                       nn.Linear(512, num_diseases))
        
    def forward(self, xb):
        out = self.conv1(xb)
        out = self.conv2(out)
        out = self.res1(out) + out
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.res2(out) + out
        out = self.classifier(out)
        return out