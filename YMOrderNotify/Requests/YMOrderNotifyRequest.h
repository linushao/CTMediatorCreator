//
//  YMOrderNotifyRequest.h
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//


#import "YMRequest.h"

@class YMOrderNotifyRequestModel;

@interface YMOrderNotifyRequest : YMRequest

- (instancetype)initWithModel:(YMOrderNotifyRequestModel *)model;

@end



@interface YMOrderNotifyRequestModel : NSObject

//@property (nonatomic, copy) NSString *<#Text#>;

@end