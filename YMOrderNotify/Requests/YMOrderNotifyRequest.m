//
//  YMOrderNotifyRequest.m
//  Created by ace on 2019/04/10.
//  Copyright © 2019年 ace. All rights reserved.
//

#import "YMOrderNotifyRequest.h"


@interface YMOrderNotifyRequest()

@property (nonatomic, strong) YMOrderNotifyRequestModel *model;

@end



@implementation YMOrderNotifyRequest

- (instancetype)initWithModel:(YMOrderNotifyRequestModel *)model
{
    self = [super init];
    if (self) {
        self.model = model;
    }
    return self;
}

- (NSString *)requestUrl
{
    return @"<#Text#>";
}

- (YTKRequestMethod)requestMethod
{
    return <#YTKRequestMethod#>;
}

- (void)start
{
    NSString *toastText = @"";
    
//    if (![self.model.<#Text#> isNotBlank]) {
//        toastText = LS(@"<#Text#>");
//    }
    
    if ([toastText isNotBlank]) {
        [YMHUDView showErrorMessage:toastText dismissBlock:nil];
        return;
    }
    
    [super start];
}

- (id)requestArgument
{
    if (self.model) {
        return [self.model yy_modelToJSONObject];
    } else {
        return [super requestArgument];
    }
}

@end


@implementation YMOrderNotifyRequestModel
@end