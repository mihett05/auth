import {
  Controller,
  Post,
  Body,
  HttpException, HttpStatus,
} from '@nestjs/common';

import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('users')
export class UsersControllers {
  constructor(
    private readonly _userService: UsersService,
  ) {}

  @Post()
  async createUser(@Body() createUserDto: CreateUserDto) {
    const status = await this._userService.create(
      createUserDto.username, createUserDto.password, createUserDto.email
    );

    if (status) {
      throw new HttpException(status, HttpStatus.BAD_REQUEST);
    }

    return {
      'username': createUserDto.username
    }
  }
}